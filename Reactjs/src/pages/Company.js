import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { Pagination } from "@mui/material";
import Stack from "@mui/material/Stack";
import { memo, useEffect, useState } from "react";
import Apis, { endpoints } from "../configs/Apis"
import FontCompany from "../layout/FontCompany"
import { useSearchParams } from "react-router-dom";
import { Row } from "react-bootstrap";


const Company = () => {
    const [isLoadingJobPosts, setIsLoadingJobPosts] = useState(true);
    const [q] = useSearchParams();
    const [employer, setEmployer] = useState([]);
    const [pagination, setPagination] = useState({ count: 0, sizeNumber: 0 });
    const [page, setPage] = useState(1);
    const [change, SetChange] = useState(1);
  
    useEffect(() => {
      const loadEmployer = async () => {
        try {
          let query = q.toString();
  
          query === "" ? (query += `page=${page}`) : (query += `&page=${page}`);
          console.info("query: " + query);
  
          const res = await Apis.get(`${endpoints["recruitment"]}?${query}`);
          const data = await res.data;
  
          setEmployer(data.results);
          SetChange(employer.count)
          setPagination({
            count: data.count,
            sizeNumber: Math.ceil(data.count / 2),
          });
          setIsLoadingJobPosts(false);
        } catch (err) {
          console.error(err);
        }
      };
      loadEmployer();
    }, [q, page, change]);
  
    const handleChangePage = (event, value) => {
      setPage(value);
    };
  
    console.log(
      "CardJobPostMain: Đã vào đây. Page số: " +
        page +
        ", is loading: " +
        isLoadingJobPosts
    );
  
    return (
      <Box>
        <Typography
          component="h4"
          variant="h4"
          align="center"
          color="text.primary"
          gutterBottom
          sx={{ marginBottom: 5 }}
        >
        </Typography>
        <Box>
          <Grid container spacing={2}>
                <><h1 className="text-center">ALL Jobs</h1><Row>
                                    {employer.map(c => <FontCompany obj={c} />)}
                                </Row></>
  
          </Grid>
        </Box>
        {pagination.sizeNumber >= 2 && (
          <Box sx={{ pt: 5, pb: 2 }}>
            <Stack>
              <Pagination
                count={pagination.sizeNumber}
                color="primary"
                size="large"
                variant="outlined"
                sx={{ margin: "0 auto" }}
                page={page}
                onChange={handleChangePage}
              />
            </Stack>
          </Box>
        )}
      </Box>
    );
  };
  
  export default memo(Company);

